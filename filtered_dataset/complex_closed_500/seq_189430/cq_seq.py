import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.227, 0.0045).lineTo(-0.227, 0.0125).lineTo(-0.227, 0.1845).threePointArc((-0.22407, 0.19157), (-0.217, 0.1945)).lineTo(-0.005, 0.1945).threePointArc((0.00207, 0.19157), (0.005, 0.1845)).lineTo(0.005, 0.0045).threePointArc((0.00235, -0.00228), (-0.0042, -0.00547)).threePointArc((-0.00477, -0.0057), (-0.00509, -0.00622)).threePointArc((-0.00615, -0.00786), (-0.008, -0.0085)).lineTo(-0.214, -0.0085).threePointArc((-0.21585, -0.00786), (-0.21691, -0.00622)).threePointArc((-0.21723, -0.0057), (-0.2178, -0.00547)).threePointArc((-0.22435, -0.00228), (-0.227, 0.0045)).close()
solid=wp_sketch0.add(loop0).extrude(0.5380505565719261)
