# Model Evaluation Report

## Dataset Sample
| Image | Description |
|-------|-------------|
| ![](media/CHSDM-26801_02-000001.jpg) | Side view of a garden sleigh, high-backed seat decorated with bands of foliage, curved sleigh back decorated with acanthus leaves. |
| ![](media/CHSDM-8B886B411AA82-000001.jpg) | Child in water, center, with a bird overhead. School master at left, in front of a building. Woman with a vase under a tree, right. |
| ![](media/CHSDM-41EB9EFB4FB32-000001.jpg) | Horizontal rectangle. Thirty-seven tiles wide and twenty-one high with opening for door or window nineteen and one-half tiles high and twelve wide. To left and right of opening, centered canopy above. Left, woman representing Hope, right, a sculputure urn. Centered above opening, a mascaron. Arabesque design of foliage. |
| ![](media/CHSDM-9DD80152F1092-000001.jpg) | Running design for a frieze or a dado, composed of scrolls of foliage and strapwork, and four repeating motifs--a seated woman in a small upright oval medallion, a putto seated on a rocailled base, and strapwork in axial pattern. The various panels, A to F, show various repeats of the same design, all being five tiles high and a varying number of tiles wide. |
| ![](media/CHSDM-5F3AB1E04B382-000001.jpg) | Incomplete drawing of a church facade with a side tower (at left). The most finished section of the drawing is at the lower left. Two stories facade with series of columns and pilasters alternating with arches and windows. |
## Model: blip-image-captioning-base-8bit-pre-peft
Sample Descriptions:
| Image | Generated Description | Human Description |
|-|-|-|
| ![](media/CHSDM-26801_02-000001.jpg) | a book with drawings of various objects | Side view of a garden sleigh, high-backed seat decorated with bands of foliage, curved sleigh back decorated with acanthus leaves. |
| ![](media/CHSDM-8B886B411AA82-000001.jpg) | a painting of a man and a woman | Child in water, center, with a bird overhead. School master at left, in front of a building. Woman with a vase under a tree, right. |
| ![](media/CHSDM-41EB9EFB4FB32-000001.jpg) | a square tile with a pattern of flowers | Horizontal rectangle. Thirty-seven tiles wide and twenty-one high with opening for door or window nineteen and one-half tiles high and twelve wide. To left and right of opening, centered canopy above. Left, woman representing Hope, right, a sculputure urn. Centered above opening, a mascaron. Arabesque design of foliage. |
| ![](media/CHSDM-9DD80152F1092-000001.jpg) | a white box with a drawing on it | Running design for a frieze or a dado, composed of scrolls of foliage and strapwork, and four repeating motifs--a seated woman in a small upright oval medallion, a putto seated on a rocailled base, and strapwork in axial pattern. The various panels, A to F, show various repeats of the same design, all being five tiles high and a varying number of tiles wide. |
| ![](media/CHSDM-5F3AB1E04B382-000001.jpg) | a drawing of a building with a tower | Incomplete drawing of a church facade with a side tower (at left). The most finished section of the drawing is at the lower left. Two stories facade with series of columns and pilasters alternating with arches and windows. |

Metrics:
| Metric | Score |
|--------|-------|
| rouge1 | `0.15169135440680864` |
| rouge2 | `0.018009523644739647` |
| rougeL | `0.12236904042536356` |
| rougeLsum | `0.12243451081859141` |
| bleu_bleu | `0.00026601008683272516` |
| bleu_precisions | `[0.3594302120141343, 0.04516088955149708, 0.004189150809429139, 0.00024855012427506213]` |
| bleu_brevity_penalty | `0.023330220490523235` |
| bleu_length_ratio | `0.21017208768000742` |
| bleu_translation_length | `18112` |
| bleu_reference_length | `86177` |
| wer | `0.9404737608337755` |
| meteor | `0.0548446395819356` |
## Model: blip-image-captioning-base-quantized
Sample Descriptions:
| Image | Generated Description | Human Description |
|-|-|-|
| ![](media/CHSDM-26801_02-000001.jpg) | a book with drawings of various objects | Side view of a garden sleigh, high-backed seat decorated with bands of foliage, curved sleigh back decorated with acanthus leaves. |
| ![](media/CHSDM-8B886B411AA82-000001.jpg) | a painting of a man and a woman | Child in water, center, with a bird overhead. School master at left, in front of a building. Woman with a vase under a tree, right. |
| ![](media/CHSDM-41EB9EFB4FB32-000001.jpg) | a square tile with a pattern of flowers | Horizontal rectangle. Thirty-seven tiles wide and twenty-one high with opening for door or window nineteen and one-half tiles high and twelve wide. To left and right of opening, centered canopy above. Left, woman representing Hope, right, a sculputure urn. Centered above opening, a mascaron. Arabesque design of foliage. |
| ![](media/CHSDM-9DD80152F1092-000001.jpg) | a white box with a drawing on it | Running design for a frieze or a dado, composed of scrolls of foliage and strapwork, and four repeating motifs--a seated woman in a small upright oval medallion, a putto seated on a rocailled base, and strapwork in axial pattern. The various panels, A to F, show various repeats of the same design, all being five tiles high and a varying number of tiles wide. |
| ![](media/CHSDM-5F3AB1E04B382-000001.jpg) | a drawing of a building with a tower | Incomplete drawing of a church facade with a side tower (at left). The most finished section of the drawing is at the lower left. Two stories facade with series of columns and pilasters alternating with arches and windows. |

Metrics:
| Metric | Score |
|--------|-------|
| rouge1 | `0.15169135440680864` |
| rouge2 | `0.018009523644739647` |
| rougeL | `0.12236904042536356` |
| rougeLsum | `0.12243451081859141` |
| bleu_bleu | `0.00026601008683272516` |
| bleu_precisions | `[0.3594302120141343, 0.04516088955149708, 0.004189150809429139, 0.00024855012427506213]` |
| bleu_brevity_penalty | `0.023330220490523235` |
| bleu_length_ratio | `0.21017208768000742` |
| bleu_translation_length | `18112` |
| bleu_reference_length | `86177` |
| wer | `0.9404737608337755` |
| meteor | `0.0548446395819356` |
## Model: blip-image-captioning-base-finetuned
Sample Descriptions:
| Image | Generated Description | Human Description |
|-|-|-|
| ![](media/CHSDM-26801_02-000001.jpg) | a - - -, blue, blue, blue, and, blue, blue, blue, blue,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, ',,, ','''''''''''''''''''''''''''''''''''''''''''''''' ' | Side view of a garden sleigh, high-backed seat decorated with bands of foliage, curved sleigh back decorated with acanthus leaves. |
| ![](media/CHSDM-8B886B411AA82-000001.jpg) | a - - -, blue, blue, blue, and, blue, blue,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, ',,,,,,,'''''''''''''''''''''''''''''''''''''''''''''''' | Child in water, center, with a bird overhead. School master at left, in front of a building. Woman with a vase under a tree, right. |
| ![](media/CHSDM-41EB9EFB4FB32-000001.jpg) | a - - -, blue, blue, blue, and,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''''''''''''''''''''''''''''''''''''''''''''''''''' ' | Horizontal rectangle. Thirty-seven tiles wide and twenty-one high with opening for door or window nineteen and one-half tiles high and twelve wide. To left and right of opening, centered canopy above. Left, woman representing Hope, right, a sculputure urn. Centered above opening, a mascaron. Arabesque design of foliage. |
| ![](media/CHSDM-9DD80152F1092-000001.jpg) | a - - -, blue, blue, blue, and, blue, blue, and,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''''''''''''''''''''''''''''''''''''''''''''''''''''' ' | Running design for a frieze or a dado, composed of scrolls of foliage and strapwork, and four repeating motifs--a seated woman in a small upright oval medallion, a putto seated on a rocailled base, and strapwork in axial pattern. The various panels, A to F, show various repeats of the same design, all being five tiles high and a varying number of tiles wide. |
| ![](media/CHSDM-5F3AB1E04B382-000001.jpg) | a - - -, blue, blue, blue, and, blue, blue, and,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, ',,, ',, ','''''''''''''''''''''''''''''''''''''''''''''''''''' | Incomplete drawing of a church facade with a side tower (at left). The most finished section of the drawing is at the lower left. Two stories facade with series of columns and pilasters alternating with arches and windows. |

Metrics:
| Metric | Score |
|--------|-------|
| rouge1 | `0.0898984095478053` |
| rouge2 | `0.00245942550117636` |
| rougeL | `0.08157798829150723` |
| rougeLsum | `0.08163135194954568` |
| bleu_bleu | `0.0006181835165838115` |
| bleu_precisions | `[0.028383105569771874, 0.001788541002816438, 0.00013800527180138282, 2.0845638050237988e-05]` |
| bleu_brevity_penalty | `1.0` |
| bleu_length_ratio | `3.4100978219246434` |
| bleu_translation_length | `293872` |
| bleu_reference_length | `86177` |
| wer | `0.9839857409145951` |
| meteor | `0.03864922325319841` |
## Model: Salesforce/blip-image-captioning-base
Sample Descriptions:
| Image | Generated Description | Human Description |
|-|-|-|
| ![](media/CHSDM-26801_02-000001.jpg) | a book with drawings of various objects | Side view of a garden sleigh, high-backed seat decorated with bands of foliage, curved sleigh back decorated with acanthus leaves. |
| ![](media/CHSDM-8B886B411AA82-000001.jpg) | a painting of a man and woman with birds | Child in water, center, with a bird overhead. School master at left, in front of a building. Woman with a vase under a tree, right. |
| ![](media/CHSDM-41EB9EFB4FB32-000001.jpg) | a square tile with a pattern of flowers | Horizontal rectangle. Thirty-seven tiles wide and twenty-one high with opening for door or window nineteen and one-half tiles high and twelve wide. To left and right of opening, centered canopy above. Left, woman representing Hope, right, a sculputure urn. Centered above opening, a mascaron. Arabesque design of foliage. |
| ![](media/CHSDM-9DD80152F1092-000001.jpg) | a white box with a drawing of a clock | Running design for a frieze or a dado, composed of scrolls of foliage and strapwork, and four repeating motifs--a seated woman in a small upright oval medallion, a putto seated on a rocailled base, and strapwork in axial pattern. The various panels, A to F, show various repeats of the same design, all being five tiles high and a varying number of tiles wide. |
| ![](media/CHSDM-5F3AB1E04B382-000001.jpg) | a drawing of a building with a tower | Incomplete drawing of a church facade with a side tower (at left). The most finished section of the drawing is at the lower left. Two stories facade with series of columns and pilasters alternating with arches and windows. |

Metrics:
| Metric | Score |
|--------|-------|
| rouge1 | `0.15186823073514133` |
| rouge2 | `0.017902226592242602` |
| rougeL | `0.12313704422673748` |
| rougeLsum | `0.12318734933322859` |
| bleu_bleu | `0.00029273979192081937` |
| bleu_precisions | `[0.36352019556642035, 0.045042227087894904, 0.0040798797509126045, 0.00041816509157815507]` |
| bleu_brevity_penalty | `0.02264362090919419` |
| bleu_length_ratio | `0.2088608329368625` |
| bleu_translation_length | `17999` |
| bleu_reference_length | `86177` |
| wer | `0.9374532293835123` |
| meteor | `0.055119699491324045` |
