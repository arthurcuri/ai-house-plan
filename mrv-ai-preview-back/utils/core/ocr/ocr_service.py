
"""
OCR Service - Serviço de Reconhecimento Óptico de Caracteres
Utiliza EasyOCR para extração de texto de imagens.
"""

import easyocr
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path
import io
from PIL import Image
import numpy as np

class OCRService:
    """Serviço de OCR usando EasyOCR"""
    
    def __init__(self):
        """Inicializar EasyOCR."""
        self.reader = easyocr.Reader(['pt', 'en'])
    
    def extract_text_from_image(self, image_data: bytes) -> List[Dict[str, Any]]:
        """
        Extrai texto de uma imagem
        
        Args:
            image_data: Dados da imagem em bytes
            
        Returns:
            Lista de dicionários com texto e coordenadas
        """
        try:
            # Converter bytes para array numpy
            image = Image.open(io.BytesIO(image_data))
            image_array = np.array(image)
            
            # Extrair texto usando EasyOCR
            results = self.reader.readtext(image_array)
            
            # Formatar resultados
            extracted_data = []
            for bbox, text, confidence in results:
                extracted_data.append({
                    'text': text,
                    'confidence': float(confidence),
                    'bbox': bbox
                })
            
            return extracted_data
            
        except Exception as e:
            logging.error(f"Erro ao extrair texto: {e}")
            return []
    
    def extract_text_from_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Extrai texto de um arquivo de imagem
        
        Args:
            file_path: Caminho para o arquivo
            
        Returns:
            Lista de dicionários com texto e coordenadas
        """
        try:
            # Ler arquivo
            with open(file_path, 'rb') as f:
                image_data = f.read()
            
            return self.extract_text_from_image(image_data)
            
        except Exception as e:
            logging.error(f"Erro ao processar arquivo {file_path}: {e}")
            return []

# Manter compatibilidade com código legado
reader = easyocr.Reader(['pt', 'en'], gpu=False)