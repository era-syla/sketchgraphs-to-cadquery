import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.001, -0.00059).lineTo(0.001, 0.0).lineTo(0.00048, -0.00029).lineTo(0.001, -0.00059).close()
solid=wp_sketch0.add(loop0).extrude(-0.0007244815997845234)
