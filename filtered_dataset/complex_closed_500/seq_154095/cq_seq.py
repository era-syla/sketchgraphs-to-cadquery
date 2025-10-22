import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00444, 0.02601).lineTo(0.01216, 0.02601).lineTo(0.01216, 0.01781).lineTo(0.00444, 0.01781).lineTo(0.00444, 0.02601).close()
solid=wp_sketch0.add(loop0).extrude(-0.019920261136477876)
