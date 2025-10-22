import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00194, -0.01415).lineTo(0.03243, -0.01415).lineTo(0.03243, 0.02485).lineTo(-0.00194, 0.02485).lineTo(-0.00194, -0.01415).close()
solid=wp_sketch0.add(loop0).extrude(0.09984697041474486)
