import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02297, 0.01324).lineTo(0.0134, 0.0228).lineTo(0.01036, 0.0228).lineTo(0.00074, 0.01318).lineTo(0.02297, 0.01324).close()
solid=wp_sketch0.add(loop0).extrude(-0.03279264478885273)
