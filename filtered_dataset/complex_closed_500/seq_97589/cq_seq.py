import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.017, 0.022).lineTo(-0.017, 0.022).threePointArc((-0.02054, 0.02054), (-0.022, 0.017)).lineTo(-0.022, -0.017).threePointArc((-0.02054, -0.02054), (-0.017, -0.022)).lineTo(0.017, -0.022).threePointArc((0.02054, -0.02054), (0.022, -0.017)).lineTo(0.022, 0.017).threePointArc((0.02054, 0.02054), (0.017, 0.022)).close()
solid=wp_sketch0.add(loop0).extrude(0.03132019824015917)
