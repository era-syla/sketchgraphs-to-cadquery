import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01619, 0.02762).lineTo(-0.01619, 0.02762).lineTo(-0.02174, 0.02762).threePointArc((-0.02295, 0.02852), (-0.02244, 0.02995)).threePointArc((-0.01785, 0.03498), (-0.01619, 0.04159)).lineTo(-0.01619, 0.05302).lineTo(0.01619, 0.05302).lineTo(0.01619, 0.04159).threePointArc((0.01785, 0.03498), (0.02244, 0.02995)).threePointArc((0.02295, 0.02852), (0.02174, 0.02762)).lineTo(0.01619, 0.02762).close()
solid=wp_sketch0.add(loop0).extrude(-0.11418459782085479)
