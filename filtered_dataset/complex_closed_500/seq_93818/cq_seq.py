import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01549, -0.02391).lineTo(0.01549, -0.02391).threePointArc((0.01774, -0.02484), (0.01867, -0.02708)).lineTo(0.01867, -0.05807).threePointArc((0.01774, -0.06032), (0.01549, -0.06125)).lineTo(-0.01549, -0.06125).threePointArc((-0.01774, -0.06032), (-0.01867, -0.05807)).lineTo(-0.01867, -0.02708).threePointArc((-0.01774, -0.02484), (-0.01549, -0.02391)).close()
solid=wp_sketch0.add(loop0).extrude(0.10851295224797948)
