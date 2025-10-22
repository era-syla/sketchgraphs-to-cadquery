import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1532, -0.00314).threePointArc((0.14376, -0.00596), (0.14636, -0.01546)).lineTo(0.1532, -0.00314).close()
solid=wp_sketch0.add(loop0).extrude(-0.019286686535766574)
