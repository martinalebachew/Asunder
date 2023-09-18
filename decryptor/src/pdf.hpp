// pdf.hpp
// (C) Martin Alebachew, 2023

#include <PDF/PDFNet.h>
#include <PDF/PDFDoc.h>
#include <PDF/PDFNetInternalTools.h>
#include <iostream>

#define PDFTRON_KEY "YOUR_TRIAL_KEY_HERE"

void InitializePDFTron();
void TerminatePDFTron();

typedef unsigned char byte;

class PDF {
private:
  pdftron::PDF::PDFDoc document;

public:
  PDF(byte* buffer, size_t size);

  bool Decrypt(std::string password);
  void Save(std::string outputPath);
};
