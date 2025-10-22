import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04113, -0.00288).lineTo(-0.03199, 0.01541).threePointArc((-0.04649, 0.01124), (-0.04113, -0.00288)).close()
solid=wp_sketch0.add(loop0).extrude(-0.021255176847298607)
