import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.16525, -0.116).lineTo(-0.15225, -0.116).lineTo(-0.15225, -0.094).lineTo(-0.16525, -0.094).lineTo(-0.16525, -0.116).close()
solid=wp_sketch0.add(loop0).extrude(0.03540943407470557)
