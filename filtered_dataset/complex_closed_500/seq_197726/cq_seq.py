import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0825, 0.0).threePointArc((-0.0, 0.0825), (-0.0825, -0.0)).lineTo(-0.115, -0.14).lineTo(-0.14331, -0.14).lineTo(-0.14331, 0.15249).lineTo(0.15969, 0.15249).lineTo(0.16397, -0.14).lineTo(0.115, -0.14).lineTo(0.0825, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.44382697967553825)
