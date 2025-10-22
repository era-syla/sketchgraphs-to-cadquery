import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04091, 0.00587).lineTo(-0.02333, 0.00587).lineTo(-0.02333, -0.00326).lineTo(-0.04091, -0.00326).lineTo(-0.04091, 0.00587).close()
solid=wp_sketch0.add(loop0).extrude(-0.000974671717771797)
