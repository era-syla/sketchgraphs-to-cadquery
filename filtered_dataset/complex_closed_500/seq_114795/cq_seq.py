import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02059, 0.00649).lineTo(-0.00919, 0.00649).threePointArc((-0.00883, 0.00635), (-0.00869, 0.00599)).lineTo(-0.00869, -0.00401).threePointArc((-0.00883, -0.00436), (-0.00919, -0.00451)).lineTo(-0.02059, -0.00451).threePointArc((-0.02094, -0.00436), (-0.02109, -0.00401)).lineTo(-0.02109, 0.00599).threePointArc((-0.02094, 0.00635), (-0.02059, 0.00649)).close()
solid=wp_sketch0.add(loop0).extrude(0.005593114444395324)
