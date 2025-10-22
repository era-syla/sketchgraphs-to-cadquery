import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-1.07315, -0.0889).lineTo(-1.07315, -0.1143).lineTo(-1.04775, -0.1143).lineTo(-1.04775, -0.1016).lineTo(-1.04775, -0.0889).lineTo(-1.07315, -0.0889).close()
solid=wp_sketch0.add(loop0).extrude(0.010148846395673063)
