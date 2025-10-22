import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.04, 0.03426).lineTo(0.05, 0.03426).lineTo(0.05, 0.00926).lineTo(0.04, 0.00926).lineTo(0.04, 0.03426).close()
solid=wp_sketch0.add(loop0).extrude(-0.00825605094570805)
