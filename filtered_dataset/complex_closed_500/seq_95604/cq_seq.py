import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.00238).lineTo(0.0, -0.00238).threePointArc((-0.00238, -0.0), (0.0, 0.00238)).close()
solid=wp_sketch0.add(loop0).extrude(-0.002534222725424175)
