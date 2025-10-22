import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.10741, -0.00786).lineTo(0.10741, -0.03786).lineTo(-0.02259, -0.03786).lineTo(-0.02259, -0.00786).lineTo(0.10741, -0.00786).close()
solid=wp_sketch0.add(loop0).extrude(0.26626610300103626)
