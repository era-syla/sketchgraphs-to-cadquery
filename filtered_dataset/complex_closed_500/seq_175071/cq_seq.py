import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.09215, 0.0).lineTo(0.09785, 0.0).lineTo(0.09785, 0.108).lineTo(-0.09215, 0.108).lineTo(-0.09215, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.4057824945861396)
