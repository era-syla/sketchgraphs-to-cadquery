import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0525, 0.0883).lineTo(-0.0525, 0.0833).threePointArc((-0.05104, 0.07976), (-0.0475, 0.0783)).lineTo(-0.0425, 0.0783).threePointArc((-0.03896, 0.07976), (-0.0375, 0.0833)).lineTo(-0.0375, 0.0883).lineTo(-0.0525, 0.0883).close()
solid=wp_sketch0.add(loop0).extrude(-0.01359206426423417)
