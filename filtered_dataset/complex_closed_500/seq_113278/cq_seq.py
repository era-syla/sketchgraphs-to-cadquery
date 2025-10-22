import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00359, -0.0889).lineTo(-0.00359, -0.1143).lineTo(-1.07039, -0.1143).lineTo(-1.07039, -0.0889).lineTo(-0.00359, -0.0889).close()
solid=wp_sketch0.add(loop0).extrude(-2.2121446865201433)
