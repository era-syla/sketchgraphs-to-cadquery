import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02268, -0.00877).lineTo(-0.02268, 0.02482).threePointArc((-0.0131, 0.03729), (0.0006, 0.02958)).threePointArc((0.00699, 0.02656), (0.01001, 0.03295)).threePointArc((-0.0136, 0.04734), (-0.03263, 0.02727)).lineTo(-0.04268, -0.00877).lineTo(-0.02268, -0.00877).close()
solid=wp_sketch0.add(loop0).extrude(0.0713604895423809)
