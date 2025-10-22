import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-3.9401, 8.65).lineTo(-3.9401, 8.644).lineTo(-6.794, 8.644).lineTo(-6.794, 5.39216).lineTo(-5.65942, 3.1675).lineTo(-5.66418, 3.16507).lineTo(-6.8, 5.39216).lineTo(-6.8, 8.65).lineTo(-3.9401, 8.65).close()
solid=wp_sketch0.add(loop0).extrude(7.661076603658833)
