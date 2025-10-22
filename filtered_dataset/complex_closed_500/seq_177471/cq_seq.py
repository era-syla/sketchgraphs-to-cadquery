import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0181, -0.34953).threePointArc((-0.01347, -0.34974), (-0.00885, -0.34989)).threePointArc((0.01347, 0.34974), (-0.0181, -0.34953)).close()
solid=wp_sketch0.add(loop0).extrude(0.4034205383022816)
