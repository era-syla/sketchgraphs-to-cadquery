import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.102, 0.13).lineTo(-0.102, 0.16).lineTo(-0.07467, 0.20734).lineTo(-0.02733, 0.23467).lineTo(0.02733, 0.23467).lineTo(0.07467, 0.20734).lineTo(0.102, 0.16).lineTo(0.102, 0.13).lineTo(-0.102, 0.13).close()
solid=wp_sketch0.add(loop0).extrude(0.09108934566013446)
