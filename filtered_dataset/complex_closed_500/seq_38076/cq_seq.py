import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04601, 0.00159).lineTo(-0.03489, 0.00159).threePointArc((-0.03493, -0.0), (-0.03489, -0.00159)).lineTo(-0.04601, -0.00159).threePointArc((-0.04604, -0.0), (-0.04601, 0.00159)).close()
solid=wp_sketch0.add(loop0).extrude(0.0065009100508529)
