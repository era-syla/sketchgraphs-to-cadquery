import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0198, 0.00848).lineTo(0.01439, 0.00848).lineTo(0.01439, 0.00179).lineTo(0.0198, 0.00179).lineTo(0.0198, 0.00848).close()
solid=wp_sketch0.add(loop0).extrude(-0.013500814545117845)
