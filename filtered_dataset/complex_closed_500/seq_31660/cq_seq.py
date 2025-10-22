import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.06015, 0.06033).lineTo(-0.01263, 0.06033).lineTo(-0.01263, 0.02527).lineTo(-0.06015, 0.02527).lineTo(-0.06015, 0.06033).close()
solid=wp_sketch0.add(loop0).extrude(-0.0632585006377101)
