import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0125, 0.0).lineTo(-0.0125, -0.01).lineTo(-0.0095, -0.01).lineTo(-0.0095, -0.0075).threePointArc((-0.0111, -0.005), (-0.0095, -0.0025)).lineTo(-0.0095, 0.0).lineTo(-0.0125, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.02620621015770908)
