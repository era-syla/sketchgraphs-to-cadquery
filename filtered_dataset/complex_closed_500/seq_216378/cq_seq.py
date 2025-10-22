import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02, 0.06).lineTo(-0.02, 0.02).lineTo(-0.01, 0.03).lineTo(-0.01, 0.05).lineTo(-0.02, 0.06).close()
solid=wp_sketch0.add(loop0).extrude(0.04094733024307057)
