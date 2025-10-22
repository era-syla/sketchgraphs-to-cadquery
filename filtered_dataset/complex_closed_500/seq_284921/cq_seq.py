import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03471, 0.05374).lineTo(-0.03071, 0.05374).threePointArc((-0.02321, 0.04624), (-0.03071, 0.03874)).lineTo(-0.03471, 0.03874).threePointArc((-0.04221, 0.04624), (-0.03471, 0.05374)).close()
solid=wp_sketch0.add(loop0).extrude(-0.05445531618618819)
