import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.007).threePointArc((0.003, 0.01), (0.0, 0.013)).lineTo(0.0, 0.007).close()
solid=wp_sketch0.add(loop0).extrude(0.009877281832596087)
