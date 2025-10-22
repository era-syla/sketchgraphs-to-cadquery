import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00559, -0.00301).threePointArc((0.00635, -0.0), (-0.00559, 0.00301)).threePointArc((-0.00914, -0.0), (-0.00559, -0.00301)).close()
solid=wp_sketch0.add(loop0).extrude(0.021054935902116313)
