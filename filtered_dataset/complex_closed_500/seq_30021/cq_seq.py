import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.08737, -0.31304).threePointArc((0.32496, 0.00517), (-0.09728, 0.3101)).lineTo(-0.11, 0.37384).lineTo(0.477, 0.491).lineTo(1.466, 0.491).lineTo(1.466, -0.809).lineTo(0.477, -0.592).lineTo(-0.11, -0.37397).lineTo(-0.08737, -0.31304).close()
solid=wp_sketch0.add(loop0).extrude(-1.565419518145867)
