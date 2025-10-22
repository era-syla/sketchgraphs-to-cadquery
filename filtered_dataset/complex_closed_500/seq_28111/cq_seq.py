import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.805, 0.038).lineTo(0.845, 0.038).lineTo(0.845, -0.039).lineTo(0.805, -0.039).lineTo(0.805, 0.038).close()
solid=wp_sketch0.add(loop0).extrude(-0.02275012562285622)
