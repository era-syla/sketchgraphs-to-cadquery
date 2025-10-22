import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.1237, -0.10113).lineTo(0.06434, -0.10113).threePointArc((0.08032, -0.06863), (0.06434, -0.03613)).lineTo(-0.1237, -0.03613).threePointArc((-0.13968, -0.06863), (-0.1237, -0.10113)).close()
solid=wp_sketch0.add(loop0).extrude(0.3118778909460171)
