import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.073, 0.03221).lineTo(-0.072, 0.03221).lineTo(-0.072, 0.02779).lineTo(-0.073, 0.02779).lineTo(-0.073, 0.03221).close()
solid=wp_sketch0.add(loop0).extrude(0.010522213168471054)
