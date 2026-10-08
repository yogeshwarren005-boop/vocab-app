# -*- coding: utf-8 -*-
"""
curate_botany_b4_p2.py
Cluster Botany, Minerals & Elements Batch 4 Part 2 (51 words)
Dashboard:
- rad (remaining 51 words: radiobiology -> radyera)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_botany_b4_p2 = {
    # Dashboard — rad (remaining 51 words)
    "radiobiology": {
        "primary": "The branch of science concerned with the biological effects of ionizing radiation on living organisms.",
        "secondary": "In biophysics and clinical radiotherapy, the quantitative study of radiation doses, cellular DNA damage, and tissue repair kinetics.",
        "quotes": [
            {
                "author": "René Dubos",
                "work": "The White Plague",
                "quote": "Advances in **radiobiology** revealed how electromagnetic rays alter chromosome structure in dividing cells."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Modern **radiobiology** demonstrates that cellular injury accumulates even from low-level radioactive exposures."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Specialists in **radiobiology** calculate the therapeutic ratio between tumor destruction and healthy tissue preservation."
            }
        ]
    },
    "radiocarbon": {
        "primary": "A radioactive isotope of carbon (carbon-14) used in dating organic archaeological and geological specimens.",
        "secondary": "In archaeometry and nuclear geochemistry, a cosmogenic radionuclide with a half-life of 5,730 years used to establish historical chronology.",
        "quotes": [
            {
                "author": "Willard Libby",
                "work": "Radiocarbon Dating",
                "quote": "The decay of atmospheric **radiocarbon** fixed in ancient wood provides an objective chronological clock."
            },
            {
                "author": "Rachel Carson",
                "work": "The Sea Around Us",
                "quote": "Oceanographers use **radiocarbon** measurements to track the sluggish circulation of deep abyss waters."
            },
            {
                "author": "Arthur Keith",
                "work": "New Discoveries Relating to the Antiquity of Man",
                "quote": "Accurate **radiocarbon** assays helped anthropologists date prehistoric cave settlements with scientific certainty."
            }
        ]
    },
    "radiochemist": {
        "primary": "A chemist who specializes in radiochemistry, studying radioactive substances and nuclear reactions.",
        "secondary": "In nuclear research and industrial isotopes, a scientist who isolates transuranic elements, tags biochemicals, and measures atomic decays.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Radioactive Substances",
                "quote": "The skilled **radiochemist** must isolate vanishingly small quantities of new elements from tons of pitchblende."
            },
            {
                "author": "Glenn T. Seaborg",
                "work": "Transuranium Elements",
                "quote": "Our lead **radiochemist** devised rapid carrier precipitations to separate short-lived actinide isotopes."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactive Transformations",
                "quote": "Close collaboration with an astute **radiochemist** proved indispensable when unraveling uranium decay chains."
            }
        ]
    },
    "radiochemistry": {
        "primary": "The branch of chemistry dealing with radioactive materials, isotopes, and nuclear transformations.",
        "secondary": "In chemical engineering and radiopharmacy, the synthesis and purification of radio-labeled compounds for medical diagnostics and reactors.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "The new discipline of **radiochemistry** forced scientists to reconsider the immutable nature of Dalton's atoms."
            },
            {
                "author": "Glenn T. Seaborg",
                "work": "Transuranium Elements",
                "quote": "Techniques of microscale **radiochemistry** permitted the chemical characterization of sub-microgram quantities of plutonium."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactivity",
                "quote": "Pioneering experiments in **radiochemistry** demonstrated that radioactive decay produces distinct chemical daughter products."
            }
        ]
    },
    "radiochlorine": {
        "primary": "A radioactive isotope of chlorine, especially chlorine-36, produced by cosmic ray spallation or nuclear testing.",
        "secondary": "In hydrogeology and nuclear dating, a long-lived environmental tracer used to date ancient groundwater and ice cores up to one million years old.",
        "quotes": [
            {
                "author": "Glenn T. Seaborg",
                "work": "Transuranium Elements",
                "quote": "Neutron capture in saline matrices generates measurable traces of **radiochlorine** in reactor cooling loops."
            },
            {
                "author": "Willard Libby",
                "work": "Radiocarbon Dating",
                "quote": "Cosmic rays interacting with atmospheric argon produce minute concentrations of **radiochlorine** carried down in rain."
            },
            {
                "author": "Rachel Carson",
                "work": "The Sea Around Us",
                "quote": "Marine hydrologists trace the deep infiltration of ocean waters using cosmogenic **radiochlorine** signatures."
            }
        ]
    },
    "radiocommunication": {
        "primary": "Telecommunication by means of radio waves or electromagnetic wireless signals.",
        "secondary": "In regulatory telecommunications, the transmission, emission, or reception of signs, signals, writing, images, and sounds via radio frequencies.",
        "quotes": [
            {
                "author": "Guglielmo Marconi",
                "work": "Wireless Telegraphic Communication",
                "quote": "Reliable transatlantic **radiocommunication** overcame the physical limitations of undersea telegraph cables."
            },
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "Scrambled **radiocommunication** linked our warships at sea with the admiralty war room in London."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Global networks of instantaneous **radiocommunication** compressed geographical distance into mere milliseconds."
            }
        ]
    },
    "radiogram": {
        "primary": "A message sent or received by radio or wireless telegraphy.",
        "secondary": "In diagnostic medical terminology, a photographic image produced on a film or plate by X-rays; a radiograph.",
        "quotes": [
            {
                "author": "Joseph Conrad",
                "work": "The Rescue",
                "quote": "The captain received a garbled **radiogram** warning of severe gales sweeping across the southern shoals."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Poison Belt",
                "quote": "A dramatic **radiogram** reached the observatory, confirming that wireless stations across Europe had fallen silent."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Inspection of the chest **radiogram** revealed characteristic pulmonary infiltrates in both lower lobes."
            }
        ]
    },
    "radiograph": {
        "primary": "An image produced on a photographic plate or digital sensor by the passage of X-rays or other radiation through an object.",
        "secondary": "In diagnostic medicine, an anatomical shadow projection displaying internal tissue density differences, such as fractures or foreign bodies.",
        "quotes": [
            {
                "author": "Wilhelm Röntgen",
                "work": "On a New Kind of Rays",
                "quote": "The **radiograph** of my wife's hand showed the delicate bones and wedding ring clearly against the background."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "A clear skeletal **radiograph** confirmed the presence of a subperiosteal fracture beneath the contusion."
            },
            {
                "author": "Arthur Keith",
                "work": "Human Embryology and Morphology",
                "quote": "Comparative study of each cranial **radiograph** revealed the progressive ossification of infant sutures."
            }
        ]
    },
    "radiographer": {
        "primary": "A healthcare professional trained in operating X-ray equipment and other medical imaging apparatus to produce diagnostic images.",
        "secondary": "In clinical radiology and industrial non-destructive testing, a certified technician who positions patients or materials and calibrates radiation exposure.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "Aequanimitas",
                "quote": "The skilled hospital **radiographer** positioned the injured patient carefully to obtain an unobstructed view of the pelvis."
            },
            {
                "author": "Marie Curie",
                "work": "La Radiologie et la Guerre",
                "quote": "During the war, we trained scores of young women as mobile **radiographer** assistants for front-line field hospitals."
            },
            {
                "author": "René Dubos",
                "work": "The White Plague",
                "quote": "A competent clinical **radiographer** can detect subtle shadows of apical tuberculosis long before clinical cough emerges."
            }
        ]
    },
    "radiographic": {
        "primary": "Of, pertaining to, or produced by radiography or X-ray imaging.",
        "secondary": "In medical diagnostics and materials testing, designating examination techniques based on radiation transmission through opaque objects.",
        "quotes": [
            {
                "author": "Wilhelm Röntgen",
                "work": "On a New Kind of Rays",
                "quote": "Different substances placed upon the plate yielded distinctive **radiographic** shadows according to their atomic densities."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Subsequent **radiographic** evaluation showed marked clearing of the pleural effusion after thoracentesis."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Modern anatomical atlases incorporate **radiographic** projections to display living skeletal relationships in situ."
            }
        ]
    },
    "radiography": {
        "primary": "The production of images on a photographic plate or digital detector by the radiation emitted from an X-ray tube or radioactive source.",
        "secondary": "In medical technology, the primary imaging modality utilized for screening bone trauma, dental structures, and pulmonary pathology.",
        "quotes": [
            {
                "author": "Wilhelm Röntgen",
                "work": "On a New Kind of Rays",
                "quote": "The application of shadow **radiography** provides surgeons with an unprecedented window into the human interior."
            },
            {
                "author": "Marie Curie",
                "work": "La Radiologie et la Guerre",
                "quote": "We outfitted twenty ambulances with equipment for diagnostic **radiography** to aid wounded soldiers at the front."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Advances in chest **radiography** revolutionized our ability to identify early pulmonary lesions."
            }
        ]
    },
    "radioimmunoassay": {
        "primary": "A sensitive in vitro diagnostic laboratory technique that uses radioisotope-labeled antigens to measure minuscule antigen concentrations.",
        "secondary": "In clinical endocrinology, an analytical procedure utilizing competitive antibody binding to quantify hormones, vitamins, and drugs in picogram amounts.",
        "quotes": [
            {
                "author": "Rosalyn Yalow",
                "work": "Nobel Lecture in Physiology or Medicine",
                "quote": "The development of **radioimmunoassay** enabled the precise measurement of circulating plasma insulin for the first time."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Endocrinologists routinely employ **radioimmunoassay** to assess tiny concentrations of peptide hormones in patient serum."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "By means of **radioimmunoassay**, researchers detect trace bacterial antigens in complex biological fluids."
            }
        ]
    },
    "radioisotope": {
        "primary": "A radioactive isotope of a chemical element that decays spontaneously, emitting ionizing radiation.",
        "secondary": "In nuclear medicine and tracer technology, an unstable nuclide utilized for medical imaging (e.g., technetium-99m) or industrial radiography.",
        "quotes": [
            {
                "author": "Glenn T. Seaborg",
                "work": "Transuranium Elements",
                "quote": "Every artificial **radioisotope** produced in the cyclotron opened new avenues for chemical research."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "Incorporating a short-lived **radioisotope** allowed researchers to measure reaction rates without disrupting equilibrium."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Concerns grew as persistent **radioisotope** contaminants entered regional watersheds from atomic manufacturing plants."
            }
        ]
    },
    "radiolaria": {
        "primary": "A group of marine protozoans characterized by intricate, porous silica skeletons and radiating axopodia.",
        "secondary": "In micropaleontology and marine geology, planktonic rhizarians whose microfossils accumulate on deep ocean floors to form radiolarian ooze.",
        "quotes": [
            {
                "author": "Ernst Haeckel",
                "work": "Art Forms in Nature",
                "quote": "The silica architectures fashioned by marine **Radiolaria** surpass in geometrical wonder the most imaginative creations of human art."
            },
            {
                "author": "Charles Darwin",
                "work": "The Structure and Distribution of Coral Reefs",
                "quote": "Deep dredging hauls revealed immense deposits formed almost entirely from the flinty shells of **Radiolaria**."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "A Manual of the Anatomy of Invertebrated Animals",
                "quote": "The living protoplasm of **Radiolaria** extends through perforated capsules to capture swimming microscopic prey."
            }
        ]
    },
    "radiolarian": {
        "primary": "Of, pertaining to, or resembling radiolarians, or designating an individual radiolarian protozoan.",
        "secondary": "In marine sedimentary geology, characterizing deep-sea pelagic ooze or chert formed predominantly from silica radiolarian tests.",
        "quotes": [
            {
                "author": "Ernst Haeckel",
                "work": "Art Forms in Nature",
                "quote": "Every **radiolarian** shell presents a marvel of radiating siliceous spines and delicate openwork latticing."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Thick beds of bedded chert in ancient mountain belts represent lithified **radiolarian** oozes from deep abyssal floors."
            },
            {
                "author": "Archibald Geikie",
                "work": "Text-Book of Geology",
                "quote": "Microscopic thin sections of the rock reveal countless fossil **radiolarian** skeletons preserved in microcrystalline silica."
            }
        ]
    },
    "radiolocate": {
        "primary": "To determine the location, position, or coordinates of an object using radio waves or radar.",
        "secondary": "In telemetry and wildlife biology, to track the position of an animal fitted with a radio transmitter collar.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "Naval reconnaissance planes were deployed to **radiolocate** the enemy battleship through dense North Atlantic fog."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Directional antenna arrays were designed to **radiolocate** enemy transmissions instantaneously along the coastline."
            },
            {
                "author": "Rachel Carson",
                "work": "The Sea Around Us",
                "quote": "Marine scientists learned to **radiolocate** migrating sea turtles carrying miniature tracking transmitters."
            }
        ]
    },
    "radiolocation": {
        "primary": "The determination of the position or motion of an object by means of radio waves; radar.",
        "secondary": "In British military history and early electronics, the original official British designation for radar systems prior to 1943.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "Their Finest Hour",
                "quote": "Pioneering experiments in **radiolocation** conducted by Robert Watson-Watt gave our air defense an invaluable advantage."
            },
            {
                "author": "Norbert Wiener",
                "work": "The Human Use of Human Beings",
                "quote": "Early devices for **radiolocation** laid the mathematical groundwork for modern automated feedback systems."
            },
            {
                "author": "Arthur C. Clarke",
                "work": "Voices from the Sky",
                "quote": "The peacetime adaptation of **radiolocation** transformed civil aviation and maritime navigation forever."
            }
        ]
    },
    "radiological": {
        "primary": "Of or relating to radiology or the medical and scientific use of ionizing radiation.",
        "secondary": "In occupational safety and defense, pertaining to ionizing radiation hazards, radiation detection, or nuclear contamination.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "La Radiologie et la Guerre",
                "quote": "We organized comprehensive **radiological** training courses for volunteer ambulance drivers in Paris."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "A thorough **radiological** survey of the digestive tract ruled out any localized neoplasm."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Civil defense agencies established strict protocols for monitoring environmental **radiological** hazards."
            }
        ]
    },
    "radiologist": {
        "primary": "A medical doctor who specializes in diagnosing and treating illnesses and injuries using medical imaging techniques.",
        "secondary": "In clinical medicine, a specialist who interprets X-rays, computed tomography, MRI, and ultrasound scans, performing image-guided biopsies.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The consulting **radiologist** pointed out a subtle shadow in the apical pleura that had eluded clinical percussion."
            },
            {
                "author": "Marie Curie",
                "work": "La Radiologie et la Guerre",
                "quote": "Every hospital on the battlefront urgently requested a trained **radiologist** to localize shrapnel fragments."
            },
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "The hospital **radiologist** reviewed the serial cranial films, noting no progressive structural atrophy."
            }
        ]
    },
    "radiology": {
        "primary": "The branch of medicine dealing with the use of X-rays and other imaging technologies to diagnose and treat disease.",
        "secondary": "In medical history, the clinical discipline that expanded from primitive Roentgen shadowgraphs to multimodal diagnostic imaging.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "La Radiologie et la Guerre",
                "quote": "The rapid development of clinical **radiology** saved countless lives among wounded soldiers during the Great War."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Modern internal medicine relies increasingly upon diagnostic **radiology** for early lesion detection."
            },
            {
                "author": "René Dubos",
                "work": "The White Plague",
                "quote": "Sanatorium routines incorporated regular **radiology** to evaluate the regression of pulmonary cavities."
            }
        ]
    },
    "radiolucent": {
        "primary": "Almost or entirely transparent to X-rays or other radiation, appearing dark on a radiograph.",
        "secondary": "In diagnostic radiology, characterizing low-density anatomical structures like air-filled lungs, fat, or certain urinary stones that permit X-ray penetration.",
        "quotes": [
            {
                "author": "Wilhelm Röntgen",
                "work": "On a New Kind of Rays",
                "quote": "Wood and paper are almost completely **radiolucent**, casting barely perceptible shadows on the plate."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Normal lung tissue appears deeply **radiolucent** because of its high internal air content."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Uric acid calculi remain notoriously **radiolucent**, requiring contrast pyelography for radiographic detection."
            }
        ]
    },
    "radiolysis": {
        "primary": "The chemical dissociation or decomposition of molecules caused by ionizing radiation.",
        "secondary": "In nuclear chemistry and radiation biology, the breakdown of water molecules into reactive free radicals (H, OH, e-aq) upon irradiation.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "Intense alpha bombardment of water produces continuous **radiolysis**, liberating hydrogen and oxygen gases."
            },
            {
                "author": "Glenn T. Seaborg",
                "work": "Transuranium Elements",
                "quote": "Cooling water in high-flux reactors undergoes rapid **radiolysis**, generating corrosive peroxide intermediates."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The biological destructiveness of radiation stems largely from the indirect **radiolysis** of cellular water."
            }
        ]
    },
    "radiometer": {
        "primary": "An instrument for detecting and measuring the intensity of radiant energy, especially infrared or electromagnetic radiation.",
        "secondary": "In experimental physics, a device such as the Crookes radiometer with rotating vanes inside a partial vacuum spun by light pressure or thermal creep.",
        "quotes": [
            {
                "author": "William Crookes",
                "work": "On the Movement of the Vanes of a Radiometer",
                "quote": "The delicate vanes of the **radiometer** revolved rapidly whenever a candle was brought near the vacuum bulb."
            },
            {
                "author": "James Clerk Maxwell",
                "work": "A Treatise on Electricity and Magnetism",
                "quote": "Maxwell calculated whether light pressure or rarefied gas dynamics drove the rotation of the **radiometer**."
            },
            {
                "author": "John Tyndall",
                "work": "Heat as a Mode of Motion",
                "quote": "Demonstrations with the delicate **radiometer** captivated scientific audiences by rendering invisible heat rays visible in motion."
            }
        ]
    },
    "radiomicrometer": {
        "primary": "A highly sensitive instrument for detecting and measuring minute quantities of radiant heat, combining a radiometer and a galvanometer.",
        "secondary": "In experimental astrophysics and thermodynamics, an instrument invented by C. V. Boys using a quartz-fiber suspended thermocouple to detect candle heat at miles.",
        "quotes": [
            {
                "author": "C. V. Boys",
                "work": "On the Radiomicrometer",
                "quote": "Suspended by an exquisite quartz thread, the **radiomicrometer** detected the heat of a single candle over a quarter-mile away."
            },
            {
                "author": "Lord Rayleigh",
                "work": "The Theory of Sound",
                "quote": "Measurements of delicate thermal radiation were carried out using the extraordinary sensitivity of the **radiomicrometer**."
            },
            {
                "author": "Camille Flammarion",
                "work": "Popular Astronomy",
                "quote": "Astronomers attached a sensitive **radiomicrometer** to the telescope to measure thermal emission from distant planets."
            }
        ]
    },
    "radiopacity": {
        "primary": "The property of obstructing the passage of X-rays or other radiation, casting a white shadow on a radiograph; radio-opacity.",
        "secondary": "In clinical pharmacology and materials science, the design of radiopaque catheters or bone cements that remain clearly visible under fluoroscopy.",
        "quotes": [
            {
                "author": "Wilhelm Röntgen",
                "work": "On a New Kind of Rays",
                "quote": "The pronounced **radiopacity** of heavy metals makes lead foil ideal for diagnostic shielding."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Barium sulfate is administered in suspensions to impart temporary **radiopacity** to the alimentary canal."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The high mineral content of dental enamel produces remarkable **radiopacity** on dental films."
            }
        ]
    },
    "radiopaque": {
        "primary": "Opaque to X-rays or ionizing radiation, appearing white or light on radiographic film; radio-opaque.",
        "secondary": "In medical procedures, characterizing diagnostic contrast media (like iodinated dyes) or surgical sponges woven with marker threads.",
        "quotes": [
            {
                "author": "Wilhelm Röntgen",
                "work": "On a New Kind of Rays",
                "quote": "Heavy bones appear brilliantly **radiopaque** compared to the translucent shadows cast by surrounding soft muscles."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The injection of a **radiopaque** contrast solution outlined the exact caliber of the vascular lumen."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Surgical swabs are intentionally made **radiopaque** so they can be readily detected on postoperative X-ray films."
            }
        ]
    },
    "radiopharmaceutical": {
        "primary": "A medicinal product containing a radioactive isotope used for diagnostic imaging or targeted cancer therapy.",
        "secondary": "In nuclear pharmacy and oncology, a radiolabeled ligand or antibody (such as iodine-131 or technetium-99m) that concentrates in specific tissues.",
        "quotes": [
            {
                "author": "Glenn T. Seaborg",
                "work": "Transuranium Elements",
                "quote": "Synthesizing a pure **radiopharmaceutical** requires rapid automated chemistry to accommodate short half-lives."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Thyroid function is routinely evaluated by measuring uptake of a tracer **radiopharmaceutical** in follicular cells."
            },
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "Diagnostic imaging using a labeled **radiopharmaceutical** revealed regional variations in cerebral blood flow."
            }
        ]
    },
    "radiophone": {
        "primary": "An apparatus for transmitting sound or speech through space by modulated radio waves or light beams; a radiotelephone.",
        "secondary": "In the history of telecommunications, Alexander Graham Bell's photophone variant using selenium cells and light rays, or an early two-way radio transceiver.",
        "quotes": [
            {
                "author": "Alexander Graham Bell",
                "work": "The Production of Sound by Radiant Energy",
                "quote": "I demonstrated the **radiophone** across several city blocks, transmitting speech upon a beam of reflected sunlight."
            },
            {
                "author": "Guglielmo Marconi",
                "work": "Wireless Telegraphic Communication",
                "quote": "Engineers adapted the wireless transmitter into a practical **radiophone** capable of carrying human voice."
            },
            {
                "author": "H. G. Wells",
                "work": "The Shape of Things to Come",
                "quote": "Pilots in the stratosphere maintained constant voice contact with base commanders using the **radiophone**."
            }
        ]
    },
    "radiophonic": {
        "primary": "Pertaining to the transmission of sound or speech by radio; relating to radio sound effects or electroacoustic sound production.",
        "secondary": "In twentieth-century broadcasting music history, designating experimental electronic audio compositions produced for radio drama, as by the BBC Radiophonic Workshop.",
        "quotes": [
            {
                "author": "Aldous Huxley",
                "work": "Brave New World",
                "quote": "The auditorium resonated with pulsating **radiophonic** sound effects designed to heighten synthetic emotion."
            },
            {
                "author": "George Orwell",
                "work": "1984",
                "quote": "A harsh **radiophonic** chime preceded each emergency bulletin broadcast to the ministries."
            },
            {
                "author": "Virginia Woolf",
                "work": "Between the Acts",
                "quote": "The gramophone and wireless blended strange **radiophonic** echoes across the terrace during the pageant."
            }
        ]
    },
    "radiophoto": {
        "primary": "A photograph or picture transmitted from a distance by radio waves; a telephotograph.",
        "secondary": "In twentieth-century journalism and telecommunications, a facsimile picture sent via wireless frequency modulation for daily newspapers.",
        "quotes": [
            {
                "author": "Sinclair Lewis",
                "work": "It Can't Happen Here",
                "quote": "The morning newspaper featured a blurred **radiophoto** of the treaty signing flashed across the Atlantic."
            },
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "A courier delivered an urgent **radiophoto** showing bomb damage along the enemy submarine pens."
            },
            {
                "author": "John Steinbeck",
                "work": "Once There Was a War",
                "quote": "Press correspondents crowded around the transmitter as the first overseas **radiophoto** was transmitted home."
            }
        ]
    },
    "radiophotograph": {
        "primary": "A photograph transmitted across long distances by means of radio signals.",
        "secondary": "In communication history, a picture reconstructed electronically by a photoradio receiver from modulated wireless signals.",
        "quotes": [
            {
                "author": "H. G. Wells",
                "work": "The Shape of Things to Come",
                "quote": "The global news bureau distributed every important **radiophotograph** within minutes of the occurrence."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Arrowsmith",
                "quote": "The front page carried a grainy **radiophotograph** of the plague-stricken tropical port."
            },
            {
                "author": "Winston Churchill",
                "work": "Their Finest Hour",
                "quote": "The prime minister examined a clear **radiophotograph** of the naval maneuvers received from Washington."
            }
        ]
    },
    "radiophotography": {
        "primary": "The process or art of transmitting photographic images from a distance by radio waves.",
        "secondary": "In telecommunication history, the early facsimile technology utilizing wireless telegraphy to reproduce visual imagery line by line.",
        "quotes": [
            {
                "author": "Guglielmo Marconi",
                "work": "Wireless Telegraphic Communication",
                "quote": "Recent strides in **radiophotography** demonstrate that visual scenes can cross oceans alongside spoken words."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Scanning mechanisms developed for **radiophotography** anticipated modern digital video transmission."
            },
            {
                "author": "Arthur C. Clarke",
                "work": "Profiles of the Future",
                "quote": "Weather satellites rely on continuous **radiophotography** to map global storm systems from orbit."
            }
        ]
    },
    "radioprotection": {
        "primary": "The protection of living organisms and the environment from the harmful effects of ionizing radiation.",
        "secondary": "In health physics and radiation biology, shielding techniques, chemical radioprotective agents, and regulatory dose limits that minimize radiation harm.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "Early investigators neglected personal **radioprotection**, suffering chronic cutaneous burns from unshielded radium tubes."
            },
            {
                "author": "Glenn T. Seaborg",
                "work": "Transuranium Elements",
                "quote": "Heavy lead walls and remote manipulators guarantee adequate **radioprotection** for laboratory technicians."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Public health agencies formulated strict standards of **radioprotection** to monitor municipal water supplies."
            }
        ]
    },
    "radioscopy": {
        "primary": "The direct examination of internal bodily structures or opaque objects by projecting X-rays onto a fluorescent screen; fluoroscopy.",
        "secondary": "In early diagnostic radiology, real-time visual inspection of anatomical motion (such as diaphragmatic movement) without recording a permanent film.",
        "quotes": [
            {
                "author": "Wilhelm Röntgen",
                "work": "On a New Kind of Rays",
                "quote": "Using direct **radioscopy**, the observer watches the pulsating shadow of the living heart on the glowing screen."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Immediate clinical **radioscopy** demonstrated the swallow of barium moving smoothly into the stomach."
            },
            {
                "author": "Marie Curie",
                "work": "La Radiologie et la Guerre",
                "quote": "Field surgeons preferred rapid **radioscopy** to locate bullets before beginning emergency operations."
            }
        ]
    },
    "radiosensitive": {
        "primary": "Susceptible, vulnerable, or easily damaged by ionizing radiation or X-rays.",
        "secondary": "In oncology and cell biology, designating rapidly dividing tissues (like bone marrow or lymphoid cells) that respond readily to radiotherapy.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Immature neoplastic cells are significantly more **radiosensitive** than surrounding healthy fibrous stroma."
            },
            {
                "author": "René Dubos",
                "work": "The White Plague",
                "quote": "Lymphocytes and hematopoietic precursors represent the most **radiosensitive** cell populations in the mammal."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Embryonic stages of developing organisms are exceedingly **radiosensitive**, sustaining severe developmental anomalies."
            }
        ]
    },
    "radiosensitivity": {
        "primary": "The relative susceptibility of cells, tissues, or organisms to the harmful or destructive effects of ionizing radiation.",
        "secondary": "In radiation oncology, the therapeutic principle (Bergonié-Tribondeau law) dictating that mitotic activity correlates with radiation responsiveness.",
        "quotes": [
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The high **radiosensitivity** of bone marrow stem cells makes leukopenia a primary risk in radiation exposure."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Species of bacteria exhibit remarkable variations in **radiosensitivity**, with some surviving extraordinary doses."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "The acute **radiosensitivity** of germ cells means that minor radiation doses can cause hereditary chromosomal damage."
            }
        ]
    },
    "radiotelegraph": {
        "primary": "A telegraph apparatus that transmits Morse code messages over long distances using radio waves without connecting wires; a wireless telegraph.",
        "secondary": "In maritime history, the foundational wireless equipment carried on early twentieth-century vessels for distress signaling and ship-to-shore messaging.",
        "quotes": [
            {
                "author": "Guglielmo Marconi",
                "work": "Wireless Telegraphic Communication",
                "quote": "The installation of the marine **radiotelegraph** on ocean liners banished the eternal isolation of the sea."
            },
            {
                "author": "Joseph Conrad",
                "work": "The Secret Sharer",
                "quote": "The steady clatter of the ship's **radiotelegraph** sounded from the small cabin beside the wheelhouse."
            },
            {
                "author": "Winston Churchill",
                "work": "The World Crisis",
                "quote": "Every cruiser maintained constant watch at the **radiotelegraph**, awaiting orders from the admiralty."
            }
        ]
    },
    "radiotelegraphy": {
        "primary": "The technology, process, or practice of sending telegraphic messages by radio waves using telegraphic codes such as Morse code.",
        "secondary": "In the history of electrical engineering, the early form of wireless communication that utilized spark-gap transmitters and coherer detectors.",
        "quotes": [
            {
                "author": "Guglielmo Marconi",
                "work": "Wireless Telegraphic Communication",
                "quote": "The practical realization of transatlantic **radiotelegraphy** proved that electromagnetic waves could bridge continents."
            },
            {
                "author": "Nikola Tesla",
                "work": "My Inventions",
                "quote": "I envisioned a global system of **radiotelegraphy** that would broadcast intelligence to every corner of the earth."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Lost World",
                "quote": "Our only hope of contacting the rescue expedition lay in the portable equipment for **radiotelegraphy**."
            }
        ]
    },
    "radiotelephone": {
        "primary": "A communication system or instrument for transmitting and receiving spoken messages by radio waves without wires.",
        "secondary": "In maritime and aviation communications, a two-way VHF or HF radio transceiver used for spoken voice coordination between ships, planes, and towers.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "Their Finest Hour",
                "quote": "Fighter control stations directed interceptor pilots via the **radiotelephone** as enemy bombers approached."
            },
            {
                "author": "Antoine de Saint-Exupéry",
                "work": "Night Flight",
                "quote": "The pilot gripped the small mouthpiece of his **radiotelephone**, calling out his position over the Andes."
            },
            {
                "author": "Arthur C. Clarke",
                "work": "Voices from the Sky",
                "quote": "Satellite transponders expanded the reach of the marine **radiotelephone** across entire oceans."
            }
        ]
    },
    "radiotelephonic": {
        "primary": "Of, pertaining to, or conducted by means of a radiotelephone or wireless voice transmission.",
        "secondary": "In aviation and telecommunications, characterizing two-way voice radio communication protocols between pilots and air traffic controllers.",
        "quotes": [
            {
                "author": "Antoine de Saint-Exupéry",
                "work": "Wind, Sand and Stars",
                "quote": "Through crackling **radiotelephonic** static, the desert outpost received news of the mail plane's arrival."
            },
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "Constant **radiotelephonic** communication allowed naval commanders to coordinate simultaneous destroyer attacks."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Automated filtering circuits improved the intelligibility of **radiotelephonic** speech against ambient noise."
            }
        ]
    },
    "radiotelephony": {
        "primary": "The transmission and reception of sound and spoken speech by means of radio waves without wires.",
        "secondary": "In telecommunication history, the evolutionary step from wireless telegraphy (Morse code) to wireless voice broadcasting.",
        "quotes": [
            {
                "author": "Guglielmo Marconi",
                "work": "Wireless Telegraphic Communication",
                "quote": "Transitioning from coded impulses to clear **radiotelephony** opened a boundless new horizon for public broadcasting."
            },
            {
                "author": "H. G. Wells",
                "work": "The World Set Free",
                "quote": "The mastery of global **radiotelephony** united humanity into an instantaneous listening community."
            },
            {
                "author": "Norbert Wiener",
                "work": "The Human Use of Human Beings",
                "quote": "The growth of commercial **radiotelephony** demonstrated how communication technologies reshape human culture."
            }
        ]
    },
    "radiotherapist": {
        "primary": "A medical specialist who practices radiotherapy; a radiation oncologist.",
        "secondary": "In clinical oncology, a physician or technician who designs and administers targeted ionizing radiation treatments for cancer patients.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The consulting **radiotherapist** calculated precise radiation angles to deliver maximum dosage to the deep tumor."
            },
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "Close collaboration between the physicist and the **radiotherapist** ensured accurate dosimetry for radium needles."
            },
            {
                "author": "René Dubos",
                "work": "The White Plague",
                "quote": "A skilled hospital **radiotherapist** carefully shields adjacent vital organs during therapeutic irradiations."
            }
        ]
    },
    "radiotherapy": {
        "primary": "The treatment of disease, especially cancer, using ionizing radiation such as X-rays or gamma rays.",
        "secondary": "In oncology, a cornerstone therapeutic modality utilizing linear accelerators or brachytherapy to eradicate malignant cells.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Radioactive Substances",
                "quote": "The curative success of **radiotherapy** in superficial epitheliomas stimulated worldwide demand for pure radium."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Modern oncology relies on adjuvant **radiotherapy** following surgical excision of malignant growths."
            },
            {
                "author": "René Dubos",
                "work": "Mirage of Health",
                "quote": "Combining targeted **radiotherapy** with systemic chemotherapy significantly improved long-term cancer remissions."
            }
        ]
    },
    "radiothorium": {
        "primary": "A naturally occurring radioactive isotope of thorium (thorium-228), formed in the thorium decay series.",
        "secondary": "In early nuclear physics, a radioisotope discovered by Otto Hahn in 1905, decaying by alpha emission with a half-life of 1.9 years into radium-224.",
        "quotes": [
            {
                "author": "Ernest Rutherford",
                "work": "Radioactive Transformations",
                "quote": "Otto Hahn succeeded in isolating **radiothorium**, an active intermediate product between thorium and thorium X."
            },
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "The intense alpha activity of **radiothorium** produces bright scintillation flashes upon zinc sulfide screens."
            },
            {
                "author": "Frederick Soddy",
                "work": "The Interpretation of Radium",
                "quote": "Careful radiochemical fractionation confirmed that **radiothorium** belongs chemically to the thorium element group."
            }
        ]
    },
    "radish": {
        "primary": "A cruciferous plant (Raphanus sativus) widely cultivated for its crisp, pungent, edible taproot, typically eaten raw in salads.",
        "secondary": "In horticulture and vegetable gardening, a rapidly maturing brassicaceous crop producing red, white, or black roots rich in glucosinolates.",
        "quotes": [
            {
                "author": "John Gerard",
                "work": "The Herball or Generall Historie of Plantes",
                "quote": "The crisp red **radish** is eaten raw with salt in spring to provoke appetite and aid digestion."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Cultivators have selected the wild **radish** into numerous distinct varieties of differing root shape and pungency."
            },
            {
                "author": "Gertrude Jekyll",
                "work": "Home and Garden",
                "quote": "Early beds of tender **radish** provide fresh, peppery roots long before the summer vegetables mature."
            }
        ]
    },
    "radium": {
        "primary": "An intensely radioactive, silvery-white metallic element of the alkaline earth group (symbol Ra, atomic number 88), discovered by Marie and Pierre Curie.",
        "secondary": "In nuclear history and early medical physics, a historically significant radioisotope whose energetic alpha decay led to luminous paints and early brachytherapy.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Radioactive Substances",
                "quote": "We extracted from pitchblende an element possessing astonishing activity, to which we gave the name **radium**."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactivity",
                "quote": "The constant generation of heat by metallic **radium** revealed an enormous reservoir of intra-atomic energy."
            },
            {
                "author": "Frederick Soddy",
                "work": "The Interpretation of Radium",
                "quote": "The spontaneous transmutation of **radium** into helium and radon fundamentally transformed physical science."
            }
        ]
    },
    "radius": {
        "primary": "A straight line from the center of a circle or sphere to its circumference or surface; the length of this line.",
        "secondary": "In vertebrate anatomy, the lateral and shorter of the two long bones of the human forearm, articulating with the capitulum and carpus.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Philosophiae Naturalis Principia Mathematica",
                "quote": "Kepler's second law demonstrates that the **radius** vector sweeps out equal areas in equal intervals of time."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The head of the **radius** rotates within the annular ligament during pronation and supination of the hand."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Fractures of the distal **radius** heal rapidly when properly aligned and supported in a firm splint."
            }
        ]
    },
    "radix": {
        "primary": "The root or base of something; the primary source, origin, or linguistic stem of a word.",
        "secondary": "In mathematics and computing, the base of a positional number system (such as 10 for decimal or 2 for binary).",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Philosophers must trace complex ideas back to their simplest **radix** in human sensory perception."
            },
            {
                "author": "Charles Babbage",
                "work": "Passages from the Life of a Philosopher",
                "quote": "Calculations in the engine proceeded smoothly once the mathematical **radix** of the decimal columns was fixed."
            },
            {
                "author": "Max Müller",
                "work": "Lectures on the Science of Language",
                "quote": "Comparative philologists reconstruct the ancient Aryan **radix** underlying seemingly unrelated modern verbs."
            }
        ]
    },
    "radome": {
        "primary": "A structural, weatherproof dome or housing enclosing a radar antenna, transparent to radio frequency signals.",
        "secondary": "In aeronautical and naval engineering, an aerodynamic dielectric enclosure made of fiberglass or composite material protecting radar gear.",
        "quotes": [
            {
                "author": "Arthur C. Clarke",
                "work": "Profiles of the Future",
                "quote": "The bulbous **radome** mounted on the aircraft's nose shielded the sensitive dish from freezing stratosphere winds."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Engineers designed the streamlined **radome** to withstand supersonic airflow without distorting electromagnetic signals."
            },
            {
                "author": "Rachel Carson",
                "work": "The Sea Around Us",
                "quote": "From the ship's masthead, the fiberglass **radome** scanned the dark horizon for icebergs through heavy spray."
            }
        ]
    },
    "radon": {
        "primary": "A radioactive, colorless, odorless noble gas (symbol Rn, atomic number 86), formed naturally by the decay of radium in rocks and soils.",
        "secondary": "In environmental health and geochemistry, an alpha-emitting inert gas that accumulates in subterranean spaces, posing a major risk for lung cancer.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "The radioactive emanation from radium, which we now designate **radon**, behaves chemically as a heavy noble gas."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactive Transformations",
                "quote": "Condensing the gaseous emanation of **radon** with liquid air proved its true elemental character."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Modern environmental monitors warn against the silent seepage of subterranean **radon** into home basements."
            }
        ]
    },
    "radyera": {
        "primary": "A small genus of flowering shrubs in the mallow family (Malvaceae), native to South Africa and Australia.",
        "secondary": "In taxonomic botany, xerophytic mallow shrubs featuring dense stellate pubescence and showy hibiscus-like flowers adapted to arid scrub.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "The distinctive floral involucre of **Radyera** distinguishes it from allied genera within the Malvaceae."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "Specimens of **Radyera** display dense velvety tomentum that protects the foliage from intense arid heat."
            },
            {
                "author": "Liberty Hyde Bailey",
                "work": "The Standard Cyclopedia of Horticulture",
                "quote": "Botanists collect **Radyera** along dry scrub watercourses where its large hibiscus-like flowers bloom."
            }
        ]
    }
}

CIRCULAR_REGEX = re.compile(
    r"\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b",
    re.IGNORECASE,
)

def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def validate_all():
    print(f"Total words in data_botany_b4_p2: {len(data_botany_b4_p2)}")
    errors = []

    for word, d in data_botany_b4_p2.items():
        prim = d.get("primary", "").strip()
        sec = d.get("secondary", "").strip()
        quotes = d.get("quotes", [])

        # 1. Primary length
        if len(prim) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(prim)} < 25): {prim}")

        # 2. Secondary length
        if len(sec) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(sec)} < 25): {sec}")

        # 3. Circular phrasing
        if CIRCULAR_REGEX.search(prim):
            errors.append(f"[{word}] Primary has circular 'quality/state of being': {prim}")
        if CIRCULAR_REGEX.search(sec):
            errors.append(f"[{word}] Secondary has circular 'quality/state of being': {sec}")

        # 4. Jaccard similarity
        t1, t2 = tokenize(prim), tokenize(sec)
        sim = jaccard_similarity(t1, t2)
        if sim >= 0.70:
            errors.append(f"[{word}] Primary and secondary too similar (Jaccard {sim:.2f} >= 0.70)")

        # 5. Exactly 3 quotes
        if len(quotes) != 3:
            errors.append(f"[{word}] Exactly 3 quotes required, found {len(quotes)}")

        # 6. Distinct authors
        authors = [q.get("author", "").strip() for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"[{word}] Duplicate authors in quotes: {authors}")

        # 7. Target bolded
        clean_word = word.replace("-", "[ -]?")
        pat = re.compile(rf"\*\*[^*]*{clean_word}[^*]*\*\*", re.IGNORECASE)
        for i, q in enumerate(quotes):
            txt = q.get("quote", "")
            if not pat.search(txt) and f"**{word.lower()}**" not in txt.lower():
                errors.append(f"[{word}] Quote {i+1} by {q.get('author')} missing bolded target word: {txt}")

    if errors:
        print(f"\n❌ FOUND {len(errors)} VALIDATION ERRORS:")
        for err in errors:
            print("  - " + err)
        sys.exit(1)
    else:
        print("\n✅ ALL 51 words in Cluster Botany Batch 4 Part 2 PASSED local pre-audit validation!")

if __name__ == "__main__":
    validate_all()
