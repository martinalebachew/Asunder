// pdf.cpp
// (C) Martin Alebachew, 2023

#include "pdf.hpp"

void InitializePDFTron() {
  pdftron::PDFNet::Initialize(PDFTRON_KEY);
}

void TerminatePDFTron() {
  pdftron::PDFNet::Terminate();
}

PDF::PDF(byte* buffer, size_t size) : document(buffer, size) { }

bool PDF::Decrypt(std::string password) {
  if (!document.InitStdSecurityHandler(password))
    return false;

  document.RemoveSecurity();
  return true;
}

void PDF::Save(std::string outputPath) {
  document.Save(outputPath, pdftron::SDF::SDFDoc::e_linearized);
}
