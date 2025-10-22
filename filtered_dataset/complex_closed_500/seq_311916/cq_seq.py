import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.2286, 0.1143).lineTo(-0.2286, 0.1143).lineTo(-0.2286, -0.1143).lineTo(0.2286, -0.1143).lineTo(0.2286, 0.1143).close()
solid=wp_sketch0.add(loop0).extrude(0.7886698343205283)
