import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01778, 0.0).lineTo(0.06858, 0.0).threePointArc((0.08115, -0.03035), (0.0508, -0.01778)).lineTo(-0.0, -0.01778).threePointArc((-0.01257, 0.01257), (0.01778, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(0.24338586803383827)
