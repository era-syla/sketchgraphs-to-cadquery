import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0047, -0.0144).lineTo(-0.0064, -0.0144).lineTo(-0.0064, -0.0006).lineTo(-0.0047, -0.0006).lineTo(-0.0047, -0.0144).close()
solid=wp_sketch0.add(loop0).extrude(-0.033555409799616756)
