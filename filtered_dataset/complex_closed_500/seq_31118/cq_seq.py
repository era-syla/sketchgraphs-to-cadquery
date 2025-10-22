import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.07188, 0.07137).lineTo(-0.07188, 0.07137).lineTo(-0.07188, -0.07137).lineTo(0.07188, -0.07137).lineTo(0.07188, 0.07137).close()
solid=wp_sketch0.add(loop0).extrude(0.13243683347363122)
