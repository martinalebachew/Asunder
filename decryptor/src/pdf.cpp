// pdf.cpp
// (C) Martin Alebachew, 2023

#include "pdf.hpp"

PDF::PDF(byte* buffer, size_t size) : document(buffer, size) {
  pdftron::PDFNet::Initialize(PDFTRON_KEY);
}

PDF::~PDF() {
  pdftron::PDFNet::Terminate();
}

bool PDF::Decrypt(std::string password) {
  if (!document.InitStdSecurityHandler(password))
    return false;

  document.RemoveSecurity();
  return true;
}

void PDF::Save(std::string outputPath) {
  document.Save(outputPath, pdftron::SDF::SDFDoc::e_linearized);
}
