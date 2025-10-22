import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01263, 0.02305).lineTo(0.02967, 0.02305).lineTo(0.02967, -0.01925).lineTo(-0.01263, -0.01925).lineTo(-0.01263, 0.02305).close()
solid=wp_sketch0.add(loop0).extrude(-0.0837717397098537)
