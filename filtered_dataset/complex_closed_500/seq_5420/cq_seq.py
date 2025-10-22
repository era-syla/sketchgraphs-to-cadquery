import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02051, -0.01042).threePointArc((-0.0009, -0.01679), (0.01927, -0.01255)).threePointArc((0.01499, 0.00761), (0.00123, 0.02297)).threePointArc((0.05295, -0.03448), (-0.02051, -0.01042)).close()
solid=wp_sketch0.add(loop0).extrude(0.12376553516439291)
