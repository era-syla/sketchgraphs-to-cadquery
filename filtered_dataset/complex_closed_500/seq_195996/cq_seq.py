import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-1.47, 8.15).lineTo(-1.47, 7.98).lineTo(-1.34472, 7.98).lineTo(-1.34472, 8.03).lineTo(-1.27972, 7.965).lineTo(-1.34472, 7.9).lineTo(-1.34472, 7.95).lineTo(-1.5, 7.95).lineTo(-1.5, 8.15).lineTo(-1.72, 8.15).lineTo(-1.72, 8.18).lineTo(-1.25, 8.18).lineTo(-1.25, 8.15).lineTo(-1.47, 8.15).close()
solid=wp_sketch0.add(loop0).extrude(1.029933933840922)
