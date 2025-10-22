import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.42027, 0.04).lineTo(-0.39877, 0.075).lineTo(-0.42027, 0.075).lineTo(-0.42027, 0.04).close()
solid=wp_sketch0.add(loop0).extrude(0.0920568477399845)
