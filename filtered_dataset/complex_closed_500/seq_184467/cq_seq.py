import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0667, -0.0305).lineTo(-0.05321, -0.0305).lineTo(-0.05321, -0.009).lineTo(-0.0667, -0.009).lineTo(-0.0667, -0.0305).close()
solid=wp_sketch0.add(loop0).extrude(0.01373772475416041)
