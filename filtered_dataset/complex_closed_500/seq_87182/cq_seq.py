import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.017, 0.022).lineTo(-0.017, 0.022).threePointArc((-0.02054, 0.02054), (-0.022, 0.017)).lineTo(-0.022, -0.017).threePointArc((-0.02054, -0.02054), (-0.017, -0.022)).lineTo(0.017, -0.022).threePointArc((0.02054, -0.02054), (0.022, -0.017)).lineTo(0.022, 0.017).threePointArc((0.02054, 0.02054), (0.017, 0.022)).close()
solid=wp_sketch0.add(loop0).extrude(-0.06462070007500809)
