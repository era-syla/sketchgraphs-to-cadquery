import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04585, 0.0429).lineTo(0.01415, 0.0429).lineTo(0.01415, -0.0171).lineTo(-0.04585, -0.0171).lineTo(-0.04585, 0.0429).close()
solid=wp_sketch0.add(loop0).extrude(-0.027649858017858228)
