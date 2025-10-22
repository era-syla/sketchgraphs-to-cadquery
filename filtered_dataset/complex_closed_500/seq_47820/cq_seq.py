import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.32529, -0.01779).lineTo(0.25529, -0.01779).threePointArc((0.25175, -0.01632), (0.25029, -0.01279)).lineTo(0.25029, 0.01195).threePointArc((0.25175, 0.01548), (0.25529, 0.01695)).lineTo(0.32529, 0.01695).threePointArc((0.32882, 0.01548), (0.33029, 0.01195)).lineTo(0.33029, -0.01279).threePointArc((0.32882, -0.01632), (0.32529, -0.01779)).close()
solid=wp_sketch0.add(loop0).extrude(0.0948780066658801)
